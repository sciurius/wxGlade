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

#include "MenuTest.h"

// begin wxGlade: ::extracode
// end wxGlade



MenuTestFrame::MenuTestFrame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, wxDEFAULT_FRAME_STYLE)
{
    // begin wxGlade: MenuTestFrame::MenuTestFrame
    SetTitle(wxT("All Widgets"));
    wxIcon _icon;
    _icon.CopyFromBitmap(wxArtProvider::GetBitmap(wxART_TIP, wxART_OTHER, wxSize(32, 32)));
    SetIcon(_icon);
    SetSize(wxSize(800, 417));
    test_menubar = new wxMenuBar();
    wxMenu *wxglade_tmp_menu;
    wxMenuItem *wxglade_tmp_item;
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(wxID_OPEN, wxT("&Open"), wxT("Stock ID"));
    wxglade_tmp_menu->Append(wxID_HELP, wxT("Manual"), wxT("Stock ID, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::onShowManual, this, wxID_HELP);
    m_Close = wxglade_tmp_menu->Append(wxID_CLOSE, wxT("&Close file"), wxT("Stock ID, name, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::onCloseFile, this, wxID_CLOSE);
    m_Exit = wxglade_tmp_menu->Append(wxID_EXIT, wxT("E&xit"), wxT("Stock ID, name"));
    wxglade_tmp_menu->AppendSeparator();
    wxglade_tmp_menu->Append(wxID_OPEN, wxT("&Open"), wxT("Stock ID"), wxITEM_CHECK);
    wxglade_tmp_menu->Append(wxID_HELP, wxT("Manual"), wxT("Stock ID, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::onShowManual, this, wxID_HELP);
    m_Close = wxglade_tmp_menu->Append(wxID_CLOSE, wxT("&Close file"), wxT("Stock ID, name, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::onCloseFile, this, wxID_CLOSE);
    m_Exit = wxglade_tmp_menu->Append(wxID_EXIT, wxT("E&xit"), wxT("Stock ID, name"), wxITEM_CHECK);
    wxMenu* wxglade_tmp_menu_sub = new wxMenu();
    wxglade_tmp_menu_sub->Append(wxID_OPEN, wxT("&Open"), wxT("Stock ID"), wxITEM_RADIO);
    wxglade_tmp_menu_sub->Append(wxID_HELP, wxT("Manual"), wxT("Stock ID, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::onShowManual, this, wxID_HELP);
    m_Close = wxglade_tmp_menu_sub->Append(wxID_CLOSE, wxT("&Close file"), wxT("Stock ID, name, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::onCloseFile, this, wxID_CLOSE);
    m_Exit = wxglade_tmp_menu_sub->Append(wxID_EXIT, wxT("E&xit"), wxT("Stock ID, name"), wxITEM_RADIO);
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Radio"), wxglade_tmp_menu_sub, wxEmptyString);
    test_menubar->Append(wxglade_tmp_menu, wxT("&Stock IDs"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(mn_ID1, wxT("Named 1"), wxT("Named ID"));
    wxglade_tmp_menu->Append(mn_ID2, wxT("Named 2"), wxT("Named ID, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_named2, this, mn_ID2);
    m_named = wxglade_tmp_menu->Append(mn_ID3, wxT("Named 3"), wxT("Named ID, name, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_named3, this, mn_ID3);
    m_named4 = wxglade_tmp_menu->Append(mn_ID4, wxT("Named 4"), wxT("Named ID, name"));
    wxglade_tmp_menu->AppendSeparator();
    wxglade_tmp_menu->Append(mn_ID1C, wxT("Named 1"), wxT("Named ID"), wxITEM_CHECK);
    wxglade_tmp_menu->Append(mn_ID2C, wxT("Named 2"), wxT("Named ID, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_named2, this, mn_ID2C);
    m_named3C = wxglade_tmp_menu->Append(mn_ID3C, wxT("Named 3"), wxT("Named ID, name, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_named3, this, mn_ID3C);
    m_named4C = wxglade_tmp_menu->Append(mn_ID4C, wxT("Named 4"), wxT("Named ID, name"), wxITEM_CHECK);
    wxMenu* wxglade_tmp_menu_sub = new wxMenu();
    wxglade_tmp_menu_sub->Append(mn_ID1R, wxT("Named 1"), wxT("Named ID"), wxITEM_RADIO);
    wxglade_tmp_menu_sub->Append(mn_ID2R, wxT("Named 2"), wxT("Named ID, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_named2, this, mn_ID2R);
    m_named3R = wxglade_tmp_menu_sub->Append(mn_ID3R, wxT("Named 3"), wxT("Named ID, name, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_named3, this, mn_ID3R);
    m_named4R = wxglade_tmp_menu_sub->Append(mn_ID4R, wxT("Named 4"), wxT("Named ID, name"), wxITEM_RADIO);
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Radio"), wxglade_tmp_menu_sub, wxEmptyString);
    test_menubar->Append(wxglade_tmp_menu, wxT("&Named ID"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 1"), wxT("Auto ID"));
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 2"), wxT("Auto ID, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto2, this, wxglade_tmp_item->GetId());
    m_auto3 = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 3"), wxT("Auto ID, name, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto3, this, m_auto3->GetId());
    m_auto4 = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 4"), wxT("Auto ID, name"));
    wxglade_tmp_menu->AppendSeparator();
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 1"), wxT("Auto ID"), wxITEM_CHECK);
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 2"), wxT("Auto ID, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto2, this, wxglade_tmp_item->GetId());
    m_auto3C = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 3"), wxT("Auto ID, name, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto3, this, m_auto3C->GetId());
    m_auto4C = wxglade_tmp_menu->Append(wxID_ANY, wxT("Auto 4"), wxT("Auto ID, name"), wxITEM_CHECK);
    wxMenu* wxglade_tmp_menu_sub = new wxMenu();
    wxglade_tmp_menu_sub->Append(wxID_ANY, wxT("Auto 1"), wxT("Auto ID"), wxITEM_RADIO);
    wxglade_tmp_item = wxglade_tmp_menu_sub->Append(wxID_ANY, wxT("Auto 2"), wxT("Auto ID, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto2, this, wxglade_tmp_item->GetId());
    m_auto3R = wxglade_tmp_menu_sub->Append(wxID_ANY, wxT("Auto 3"), wxT("Auto ID, name, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_auto3, this, m_auto3R->GetId());
    m_auto4R = wxglade_tmp_menu_sub->Append(wxID_ANY, wxT("Auto 4"), wxT("Auto ID, name"), wxITEM_RADIO);
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Radio"), wxglade_tmp_menu_sub, wxEmptyString);
    test_menubar->Append(wxglade_tmp_menu, wxT("&Auto ID"));
    wxglade_tmp_menu = new wxMenu();
    wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 1"), wxT("Minus1 ID"));
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 2"), wxT("Minus1 ID, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus12, this, wxglade_tmp_item->GetId());
    m_Minus13 = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 3"), wxT("Minus1 ID, name, handler"));
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus13, this, m_Minus13->GetId());
    m_Minus14 = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 4"), wxT("Minus1 ID, name"));
    wxglade_tmp_menu->AppendSeparator();
    wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 1"), wxT("Minus1 ID"), wxITEM_CHECK);
    wxglade_tmp_item = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 2"), wxT("Minus1 ID, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus12, this, wxglade_tmp_item->GetId());
    m_Minus13C = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 3"), wxT("Minus1 ID, name, handler"), wxITEM_CHECK);
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus13, this, m_Minus13C->GetId());
    m_Minus14C = wxglade_tmp_menu->Append(wxNewId(), wxT("Minus1 4"), wxT("Minus1 ID, name"), wxITEM_CHECK);
    wxMenu* wxglade_tmp_menu_sub = new wxMenu();
    wxglade_tmp_menu_sub->Append(wxNewId(), wxT("Minus1 1"), wxT("Minus1 ID"), wxITEM_RADIO);
    wxglade_tmp_item = wxglade_tmp_menu_sub->Append(wxNewId(), wxT("Minus1 2"), wxT("Minus1 ID, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus12, this, wxglade_tmp_item->GetId());
    m_Minus13R = wxglade_tmp_menu_sub->Append(wxNewId(), wxT("Minus1 3"), wxT("Minus1 ID, name, handler"), wxITEM_RADIO);
    Bind(wxEVT_MENU, &MenuTestFrame::on_Minus13, this, m_Minus13R->GetId());
    m_Minus14R = wxglade_tmp_menu_sub->Append(wxNewId(), wxT("Minus1 4"), wxT("Minus1 ID, name"), wxITEM_RADIO);
    wxglade_tmp_menu->Append(wxID_ANY, wxT("Radio"), wxglade_tmp_menu_sub, wxEmptyString);
    test_menubar->Append(wxglade_tmp_menu, wxT("&Minus1 ID"));
    SetMenuBar(test_menubar);
    Layout();
    Centre();
    // end wxGlade
}


BEGIN_EVENT_TABLE(MenuTestFrame, wxFrame)
    // begin wxGlade: MenuTestFrame::event_table
    // end wxGlade
END_EVENT_TABLE();


void MenuTestFrame::onShowManual(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::onShowManual) not implemented yet"));
}

void MenuTestFrame::onCloseFile(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::onCloseFile) not implemented yet"));
}

void MenuTestFrame::on_named2(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_named2) not implemented yet"));
}

void MenuTestFrame::on_named3(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_named3) not implemented yet"));
}

void MenuTestFrame::on_auto2(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_auto2) not implemented yet"));
}

void MenuTestFrame::on_auto3(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_auto3) not implemented yet"));
}

void MenuTestFrame::on_Minus12(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_Minus12) not implemented yet"));
}

void MenuTestFrame::on_Minus13(wxCommandEvent &event)  // wxGlade: MenuTestFrame.<event_handler>
{
    event.Skip();
    // notify the user that he hasn't implemented the event handler yet
    wxLogDebug(wxT("Event handler (MenuTestFrame::on_Minus13) not implemented yet"));
}


// wxGlade: add MenuTestFrame event handlers


class MenuTestClass: public wxApp {
public:
    bool OnInit();
};

IMPLEMENT_APP(MenuTestClass)

bool MenuTestClass::OnInit()
{
    wxInitAllImageHandlers();
    MenuTestFrame* MenuTest = new MenuTestFrame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(MenuTest);
    MenuTest->Show();
    return true;
}
