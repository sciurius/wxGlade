# generated by wxGlade 0.9.9pre on Sat Aug 10 13:49:20 2019
#
# To get wxPerl visit http://www.wxperl.it
#

use Wx qw[:allclasses];
use strict;

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
#include "bitmapFromMem.h"
#ifndef ICON_XPM
#define ICON_XPM
#include "res/multivnc.xpm"
#endif
# end wxGlade

package FrameMain;

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

    # begin wxGlade: FrameMain::new
    $style = wxDEFAULT_FRAME_STYLE
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->SetTitle(_T("Frame"));
    my $icon = &Wx::wxNullIcon;
    $icon->CopyFromBitmap(Wx::ICON(icon));
    $self->SetIcon($icon);
    $self->SetSize(Wx::Size->new(985, 852));
    
    $self->{sizer_top} = Wx::BoxSizer->new(wxHORIZONTAL);
    
    $self->{panel_top} = Wx::Panel->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxBORDER_STATIC|wxTAB_TRAVERSAL);
    $self->{sizer_top}->Add($self->{panel_top}, 1, wxEXPAND, 0);
    
    $self->SetSizer($self->{sizer_top});
    
    $self->Layout();
    # end wxGlade
    return $self;

}


# end of class FrameMain

1;

