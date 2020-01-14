#!/usr/bin/env lisp
;;;
;;; generated by wxGlade
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxCL)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxSizer)
(use-package :wxStaticText)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; end wxGlade


(defclass MyToolBar()
        ((top-window :initform nil :accessor slot-top-window)))

(defun make-MyToolBar ()
        (let ((obj (make-instance 'MyToolBar)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj MyToolBar))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: MyToolBar.__init__
        (wxToolBar_AddTool (slot-top-window obj) wxID_UP "UpDown" wxArtProvider_GetBitmap(wxART_GO_UP wxART_OTHER wxSize_Create(32 32)) wxArtProvider_GetBitmap(wxART_GO_DOWN wxART_OTHER wxSize_Create(32 32)) wxITEM_CHECK "Up or Down" "Up or Down")
        (wxToolBar_Realize (slot-toolbar-1 obj))
        ;;; end wxGlade
        )

;;; end of class MyToolBar



(defclass MyFrame()
        ((top-window :initform nil :accessor slot-top-window)
        (sizer-1 :initform nil :accessor slot-sizer-1)
        (label-1 :initform nil :accessor slot-label-1)))

(defun make-MyFrame ()
        (let ((obj (make-instance 'MyFrame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj MyFrame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: MyFrame.__init__
        (wxFrame_SetTitle (slot-top-window obj) "frame_1")
        (slot-top-window obj).wxWindow_SetSize((200, 200))
        
        (setf (slot-sizer-1 obj) (wxBoxSizer_Create wxVERTICAL))
        
        (setf (slot-label-1 obj) (wxStaticText_Create (slot-top-window obj) wxID_ANY "placeholder - every design\nneeds a toplevel window" -1 -1 -1 -1 wxALIGN_CENTER))
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-label-1 obj) 1 (logior wxALIGN_CENTER wxALL wxEXPAND) 0 nil)
        
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-1 obj))
        
        (wxFrame_layout (slot-frame-1 self))
        ;;; end wxGlade
        )

;;; end of class MyFrame


(defun init-func (fun data evt)
        (let ((frame-1 (make-MyFrame)))
        (ELJApp_SetTopWindow (slot-top-window frame-1))
        (wxWindow_Show (slot-top-window frame-1))))
;;; end of class MyApp


(unwind-protect
    (Eljapp_initializeC (wxclosure_Create #'init-func nil) 0 nil)
    (ffi:close-foreign-library "../miscellaneous/wxc-msw2.6.2.dll"))
