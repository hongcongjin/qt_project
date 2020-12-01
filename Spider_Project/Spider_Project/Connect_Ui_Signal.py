from SpiderUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QCheckBox
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from Website.Google_Simage_Parse import GoogleImageParse
import os
import logging

logger = logging.getLogger('MainConnect')
config = dict()


# parse keyword
def gen_keyword_from_str(keywordstr, sep='|'):
    if not keywordstr:
        return []
    else:
        return keywordstr.split(sep)


# This example uses QThreads, which means that the threads at the Python level
# are named something like "Dummy-1". The function below gets the Qt name of the
# current thread.
def ctname():
    return QThread.currentThread().objectName()


# Signals need to be contained in a QObject or subclass in order to be correctly
# initialized.
class Signaller(QObject):
    signal = pyqtSignal(str, logging.LogRecord)


# Output to a Qt GUI is only supposed to happen on the main thread. So, this
# handler is designed to take a slot function which is set up to run in the main
# thread. In this example, the function takes a string argument which is a
# formatted log message, and the log record which generated it. The formatted
# string is just a convenience - you could format a string for output any way
# you like in the slot function itself.
#
# You specify the slot function to do whatever GUI updates you want. The handler
# doesn't know or care about specific UI elements.
class QtHandler(logging.Handler):
    def __init__(self, slotfunc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signaller = Signaller()
        self.signaller.signal.connect(slotfunc)

    def emit(self, record):
        s = self.format(record)
        self.signaller.signal.emit(s, record)


# 用于处理ui返回的参数的dict
class MainWorker(QObject):

    @pyqtSlot()
    def start(self):
        global config
        logger.info('Started work')
        # Let the thread run until interrupted. This allows reasonably clean
        # thread termination.
        while not QThread.currentThread().isInterruptionRequested():
            for web in config:
                if web == 0:
                    config[web]['similar'] = False
                    GoogleImageParse(config[web]).main()
                elif web == 1:
                    config[web]['similar'] = True
                    GoogleImageParse(config[web]).main()
                elif web == 2 or web == 3:
                    websit = 'bing'
                elif web == 4:
                    webs = 'flickr'
            break
        logger.info('IS_FINISHED_SINGNAL')


class MainConnect(QMainWindow, Ui_MainWindow):
    COLORS = {
        logging.DEBUG: 'black',
        logging.INFO: 'blue',
        logging.WARNING: 'orange',
        logging.ERROR: 'red',
        logging.CRITICAL: 'purple',
    }
    connectme = pyqtSignal()

    def __init__(self):
        super().__init__()  # init the QMainWindow
        # init the ui
        self.initui()
        # logging.basicConfig(level=logging.INFO)
        self.handler = h = QtHandler(self.update_status)
        # Remember to use qThreadName rather than threadName in the format string.
        fs = '%(asctime)s %(name)s %(levelname)s %(message)s'
        formatter = logging.Formatter(fs)
        h.setFormatter(formatter)
        logger.addHandler(h)

        self.start_thread()

        # Set up to terminate the QThread when we exit
        self.start.clicked.connect(self.start_work)
        # self.start.clicked.connect(lambda: self.start.setEnabled(False))
        self.connectme.connect(self.worker.start)

        self.cancel.clicked.connect(self.force_quit)
        # self.cancel.clicked.connect(lambda: self.start.setEnabled(True))

    def initui(self):
        self.setupUi(self)

    def get_config_from_ui(self):

        _config = dict()
        webvalue = dict(
            savepath=self.savepath.text(),        # """ Savepath """
            keywords=gen_keyword_from_str(self.keyword.text(), '|'),        # """Keyword LIst"""
            queues=self.queueNum.value(),      # """Max Queue"""
            maxnum=self.imageNum.value(),     # Max Num
        # """Download  Method
        #   index: 0, 1, 2
        #   value: Insert&Download, Insert to DB, Download from DB
            action=self.comboBox.currentIndex(),
        )
        """Website List"""
        for index, qcbox in enumerate(self.scrollArea.findChildren(QCheckBox)):
            if qcbox.isEnabled() and qcbox.isChecked():
                _config[index] = webvalue
        return _config

    def is_config_right(self, config):
        if not config:
            self.checkBox_1.setFocus()
            return "Please choose one website at least"
        for webindex in config:
            webvalue = config[webindex]
            if not webvalue['keywords']:
                self.keyword.setFocus()
                return "Keyword is empty"
            elif not os.path.exists(webvalue['savepath']):
                self.savepath.setFocus()
                return "The Savepath is not exist !"
            elif webvalue['maxnum'] == 0:
                self.imageNum.setFocus()
                return "Please input the number of images for each keyword "

        return True

    def start_thread(self):
        self.worker = MainWorker()
        self.worker_thread = QThread()
        self.worker.setObjectName('Worker')
        self.worker_thread.setObjectName('WorkerThread')  # for qThreadName
        self.worker.moveToThread(self.worker_thread)
        # This will start an event loop in the worker thread
        self.worker_thread.start()

    def start_work(self):
        global config
        config = self.get_config_from_ui()
        _status = self.is_config_right(config)
        print(_status)
        if _status is not True:
            logger.error(_status)
            # enable start button
            return
        self.set_progress(0)
        logger.info('Start to insert and download .......')
        # Once started, the button should be disabled
        self.start.setEnabled(False)
        self.connectme.emit()

    def kill_thread(self):
        # Just tell the worker to stop, then tell it to quit and wait for that
        # to happen
        self.worker_thread.requestInterruption()
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
            # self.worker_thread.wait()
        else:
            logger.info('worker has already exited.')

    def force_quit(self):
        self.start.setEnabled(True)
        # For use when the window is closed
        if self.worker_thread.isRunning():
            self.kill_thread()
        # self.worker_thread.start()

    def set_progress(self, value):
        self.progressBar.setValue(int(value))

    @pyqtSlot(str, logging.LogRecord)
    def update_status(self, status, record):
        color = self.COLORS.get(record.levelno, 'black')
        if '##' in status:
            progress = str(status).split('##')[1].strip('\n')
            self.set_progress(int(progress))
        elif 'IS_FINISHED_SINGNAL' in status:
            self.start.setEnabled(True)
            self.force_quit()
        s = '<pre><font color="%s">%s</font></pre>' % (color, status)
        self.plainTextEdit.appendHtml(s)

    @pyqtSlot()
    def clear_display(self):
        self.set_progress(0)
        self.plainTextEdit.clear()



