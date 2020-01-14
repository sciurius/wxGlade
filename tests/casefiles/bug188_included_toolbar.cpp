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

#include "bug188_included_toolbar.h"

// begin wxGlade: ::extracode
// end wxGlade



MyFrame::MyFrame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, style)
{
    // begin wxGlade: MyFrame::MyFrame
    SetTitle(wxT("frame_1"));
    SetSize(wxSize(200, 200));
    frame_1_toolbar = new wxToolBar(this, -1);
    SetToolBar(frame_1_toolbar);
    frame_1_toolbar->AddTool(wxID_UP, wxT("UpDown"), wxArtProvider::GetBitmap(wxART_GO_UP, wxART_OTHER, wxSize(32, 32)), wxArtProvider::GetBitmap(wxART_GO_DOWN, wxART_OTHER, wxSize(32, 32)), wxITEM_CHECK, wxT("Up or Down"), wxT("Up or Down"));
    frame_1_toolbar->Realize();
    wxBoxSizer* sizer_1 = new wxBoxSizer(wxVERTICAL);
    label_1 = new wxStaticText(this, wxID_ANY, wxT("placeholder - every design\nneeds a toplevel window"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);
    sizer_1->Add(label_1, 1, wxALIGN_CENTER|wxALL|wxEXPAND, 0);
    
    SetSizer(sizer_1);
    Layout();
    // end wxGlade
}


class MyApp: public wxApp {
public:
    bool OnInit();
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    wxInitAllImageHandlers();
    MyFrame* frame_1 = new MyFrame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(frame_1);
    frame_1->Show();
    return true;
}
