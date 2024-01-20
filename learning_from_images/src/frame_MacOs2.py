import Cocoa
import Quartz
import objc
from PyObjCTools import AppHelper
import threading

class TransparentWindow(Cocoa.NSWindow):
    def initWithContentRect_styleMask_backing_defer_(self, contentRect, styleMask, bufferingType, defer):
        self = objc.super(TransparentWindow, self).initWithContentRect_styleMask_backing_defer_(contentRect, styleMask, bufferingType, defer)
        if not self:
            return None

        self.setOpaque_(False)
        self.setBackgroundColor_(Cocoa.NSColor.clearColor)
        self.setLevel_(Quartz.kCGFloatingWindowLevel)
        self.setStyleMask_(Cocoa.NSWindowStyleMaskBorderless)

        return self

    def drawRect_(self, rect):
        print("drawRect_ called")  # Debug log
        frame_width = 20
        frame_color = Cocoa.NSColor.greenColor
        frame_path = Cocoa.NSBezierPath.bezierPathWithRect_(Cocoa.NSInsetRect(self.frame(), frame_width / 2, frame_width / 2))
        frame_color.set()
        frame_path.setLineWidth_(frame_width)
        frame_path.stroke()

class AppDelegate(Cocoa.NSObject):
    def applicationDidFinishLaunching_(self, notification):
        screen_frame = Cocoa.NSScreen.mainScreen().frame()
        print(f"Screen Frame: {screen_frame}")  # Debug log
        window = TransparentWindow.alloc().initWithContentRect_styleMask_backing_defer_(screen_frame, Cocoa.NSWindowStyleMaskBorderless, Cocoa.NSBackingStoreBuffered, False)
        window.makeKeyAndOrderFront_(self)

    def quit_(self, sender):
        AppHelper.stopEventLoop()

def stop_application():
    AppHelper.stopEventLoop()

app = Cocoa.NSApplication.sharedApplication()
delegate = AppDelegate.alloc().init()
app.setDelegate_(delegate)

# Creating a menu to quit the application
mainMenu = Cocoa.NSMenu.alloc().init()
appMenuItem = Cocoa.NSMenuItem.alloc().init()
mainMenu.addItem_(appMenuItem)
app.setMainMenu_(mainMenu)

appMenu = Cocoa.NSMenu.alloc().init()
quitMenuItem = Cocoa.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "quit:", "q")
appMenu.addItem_(quitMenuItem)
appMenuItem.setSubmenu_(appMenu)

# Set the timer to stop the application after 10 seconds
threading.Timer(10.0, stop_application).start()

AppHelper.runEventLoop()
