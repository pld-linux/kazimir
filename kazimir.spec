Summary:	Kazimir is a log analyzer, fully written in Perl
Summary(hu.UTF-8):	Kazimir egy Perl-ben írt log analizáló
Name:		kazimir
Version:	1.0
Release:	0.1
License:	CeCILL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/project/kazimir/kazimir/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	ffca5547f76dbfad234ed23f535a2437
Patch0:		%{name}-env-perl.patch
URL:		http://kazimir.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kazimir looks at several logs of several different types, try to find
user defined problematic or pathologic situations in these logs and
eventually (based on user-defined configuration) does action to signal
or correct the situation.

%description -l hu.UTF-8
A Kazimir különböző típusú logokat néz, próbálja megtalálni a
felhasználó által megadott problémás vagy patológikus helyzeteket
ezekben a naplókban, és a felhasználó által megadott alkalomkor
jelzést ad vagy javítja a helyzetet.

%package -n vim-syntax-kazimir
Summary:	Vim syntax: kazimir
Group:		Applications/Editors/Vim

%description -n vim-syntax-kazimir
Vim syntax: kazimir

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/vim/syntax
install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect

install kazimir $RPM_BUILD_ROOT%{_bindir}
install kazimir.vim $RPM_BUILD_ROOT%{_datadir}/vim/syntax
install kazimir_au.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *conf* README Licence* kazimir.pdf kazimir.ps
%attr(755,root,root) %{_bindir}/kazimir

%files -n vim-syntax-kazimir
%defattr(644,root,root,755)
%{_datadir}/vim/syntax/kazimir.vim
%{_datadir}/vim/vimfiles/ftdetect/kazimir_au.vim
