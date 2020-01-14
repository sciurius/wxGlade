#!/usr/bin/perl -w -- 
#
# generated by wxGlade
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

package Frame186;

use Wx qw[:everything];
use base qw(Wx::Frame);
use strict;

use Wx::Locale gettext => '_T';
sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: Frame186::new
    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetTitle(_T("frame_1"));
    $self->SetSize(Wx::Size->new(300, 300));
    
    

    # Menu Bar

    $self->{Bug186_Frame_menubar} = Wx::MenuBar->new();
    use constant myMagicMenu => Wx::NewId();
    my $wxglade_tmp_menu;
    $self->{File} = Wx::Menu->new();
    $self->{File}->Append(myMagicMenu, _T("Magic"), "");
    $self->{Bug186_Frame_menubar}->Append($self->{File}, _T("File"));
    $self->SetMenuBar($self->{Bug186_Frame_menubar});
    
    # Menu Bar end

    
    
    # Tool Bar
    $self->{Bug186_Frame_toolbar} = Wx::ToolBar->new($self, -1);
    use constant myMagicTool => Wx::NewId();
    $self->{Bug186_Frame_toolbar}->AddTool(myMagicTool, _T("Magic"), Wx::Bitmap->new(32, 32), wxNullBitmap, wxITEM_NORMAL, _T("Do a MAGIC action"), _T("It's really MAGIC"));
    $self->{Bug186_Frame_toolbar}->Realize();
    $self->SetToolBar($self->{Bug186_Frame_toolbar});
    # Tool Bar end
    
    $self->{sizer_1} = Wx::BoxSizer->new(wxVERTICAL);
    
    $self->{sizer_2} = Wx::BoxSizer->new(wxVERTICAL);
    $self->{sizer_1}->Add($self->{sizer_2}, 1, wxEXPAND, 0);
    
    $self->{text_ctrl_1} = Wx::TextCtrl->new($self, wxID_ANY, _T("Id: automatic (default behaviour)"));
    $self->{sizer_2}->Add($self->{text_ctrl_1}, 1, wxALL|wxEXPAND, 5);
    
    $self->{text_ctrl_2} = Wx::TextCtrl->new($self, 12123, _T("Id: numeric value \"12123\""));
    $self->{sizer_2}->Add($self->{text_ctrl_2}, 1, wxALL|wxEXPAND, 5);
    
    $self->{text_ctrl_3} = Wx::TextCtrl->new($self, wxID_ANY, _T("Id: predefined identify: \"wxID_ANY\""));
    $self->{sizer_2}->Add($self->{text_ctrl_3}, 1, wxALL|wxEXPAND, 5);
    
    use constant myButtonId => Wx::NewId();
    $self->{text_ctrl_4} = Wx::TextCtrl->new($self, myButtonId, _T("Id: variable assignment \"myButtonId=?\""));
    $self->{sizer_2}->Add($self->{text_ctrl_4}, 1, wxALL|wxEXPAND, 5);
    
    $self->SetSizer($self->{sizer_1});
    
    $self->Layout();
    # end wxGlade
    return $self;

}


# end of class Frame186

1;

package MyApp;

use base qw(Wx::App);
use strict;

sub OnInit {
    my( $self ) = shift;

    Wx::InitAllImageHandlers();

    my $Bug186_Frame = Frame186->new();

    $self->SetTopWindow($Bug186_Frame);
    $Bug186_Frame->Show(1);

    return 1;
}
# end of class MyApp

package main;

unless(caller){
    my $local = Wx::Locale->new("English", "en", "en"); # replace with ??
    $local->AddCatalog("app"); # replace with the appropriate catalog name

    my $app = MyApp->new();
    $app->MainLoop();
}
