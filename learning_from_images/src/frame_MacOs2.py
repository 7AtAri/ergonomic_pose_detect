import Cocoa
import Quartz
import objc
from PyObjCTools import AppHelper
import threading

class FrameView(Cocoa.NSView):
    def initWithFrame_(self, frame):
        self = objc.super(FrameView, self).initWithFrame_(frame)
        if not self:
            return None
        # Additional initialization if needed
        return self

    def drawRect_(self, rect):
        print("Drawing frame")  # Debug log
        frame_width = 5
        offset_for_menu_bar = 36 # Adjust this value as needed

        #frame_color = Cocoa.NSColor.yellowColor()
        frame_color = Cocoa.NSColor.colorWithCalibratedRed_green_blue_alpha_(0.2, 1, 0.2, 0.3)
         # Correct usage for setting the color
        frame_color.setStroke()  # Use setStroke() for stroking paths

        # Get the original bounds of the view
        original_bounds = self.bounds()

        # Create a new rectangle for the frame, inset by frame_width / 2
        # and adjusted downward by offset_for_menu_bar
        frame_rect = Cocoa.NSMakeRect(
            original_bounds.origin.x + frame_width / 2,
            original_bounds.origin.y + frame_width / 2 ,
            original_bounds.size.width - frame_width,
            original_bounds.size.height - frame_width - offset_for_menu_bar
        )

        frame_path = Cocoa.NSBezierPath.bezierPathWithRect_(frame_rect)
        frame_path.setLineWidth_(frame_width)
        frame_path.stroke()

class TransparentWindow(Cocoa.NSWindow):
    def initWithContentRect_styleMask_backing_defer_(self, contentRect, styleMask, bufferingType, defer):
        self = objc.super(TransparentWindow, self).initWithContentRect_styleMask_backing_defer_(contentRect, styleMask, bufferingType, defer)
        
        if not self:
            return None

        self.setOpaque_(False)
        self.setBackgroundColor_(Cocoa.NSColor.clearColor())
        #self.setLevel_(Quartz.kCGFloatingWindowLevel)
        self.setLevel_(Quartz.kCGOverlayWindowLevel)
        self.setStyleMask_(Cocoa.NSWindowStyleMaskBorderless)
        self.setIgnoresMouseEvents_(True)  # Ignore mouse events

         # Set the custom view for drawing the frame
        #frameView = FrameView.alloc().initWithFrame_(contentRect)
        frameView = FrameView.alloc().initWithFrame_(self.frame())
        self.setContentView_(frameView)

        # Keep the window on top
        self.setLevel_(Quartz.kCGMaximumWindowLevelKey)

        return self



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

# Set the timer to stop the application after x seconds
x= 60
threading.Timer(x, stop_application).start()

AppHelper.runEventLoop()
