// -*- C++ -*-
//
// generated by wxGlade
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#include "FontColour.h"

// begin wxGlade: ::extracode
// end wxGlade



MyFrame::MyFrame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, wxDEFAULT_FRAME_STYLE)
{
    // begin wxGlade: MyFrame::MyFrame
    SetTitle(_("frame_1"));
    wxBoxSizer* sizer_1 = new wxBoxSizer(wxVERTICAL);
    text_ctrl_1 = new wxTextCtrl(this, wxID_ANY, _("Some Input"), wxDefaultPosition, wxDefaultSize, wxTE_READONLY);
    text_ctrl_1->SetFont(wxFont(16, wxDEFAULT, wxNORMAL, wxBOLD, 0, wxT("")));
    text_ctrl_1->SetBackgroundColour(wxColour(0, 255, 127));
    text_ctrl_1->SetForegroundColour(wxColour(255, 0, 0));
    text_ctrl_1->SetFocus();
    sizer_1->Add(text_ctrl_1, 1, wxALL|wxEXPAND, 5);
    
    SetSizer(sizer_1);
    sizer_1->Fit(this);
    Layout();
    // end wxGlade
}


class MyApp: public wxApp {
public:
    bool OnInit();
protected:
    wxLocale m_locale;  // locale we'll be using
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    m_locale.Init();
#ifdef APP_LOCALE_DIR
    m_locale.AddCatalogLookupPathPrefix(wxT(APP_LOCALE_DIR));
#endif
    m_locale.AddCatalog(wxT(APP_CATALOG));

    wxInitAllImageHandlers();
    MyFrame* frame_1 = new MyFrame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(frame_1);
    frame_1->Show();
    return true;
}
