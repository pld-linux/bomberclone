%define _serv_ver	0.2.2
%define	_mserv	bomberclonemserv-%{_serv_ver}
Summary:	Clone of the game AtomicBomberMan
Summary(pl):	Klon gry AtomicBomberMan
Name:		bomberclone
Version:	0.11.2
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	4ba700b22bf704b15a4e8db38054e1d0
Source1:	http://dl.sourceforge.net/%{name}/%{_mserv}.tgz
# Source1-md5:	40bbe14055010e7fcf11c6bfd4e4c006
#Source2:	%{name}.desktop
Patch0:		%{name}mserv-include.patch
URL:		http://www.bomberclone.de/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clone of the game AtomicBomberMan. It supports multiplayer over the
Internet.

%description -l pl
Klon gry AtomicBomberMan wspieraj±cy grê z kilkoma graczami w
Internecie.

%package master_server
Summary:	Master server for BomberClone
Summary(pl):	G³ówny serwer dla BomberClone'a
Group:		X11/Applications/Games

%description master_server
The BomberCloneMasterServer holds a list of all active running games.
Other players can so easy join a running game by selecting the game
from join menu.

%description master_server -l pl
BomberCloneMasterServer jest g³ównym serwerem, który przechowuje
wszystkie aktywne gry. Inni gracze mog± w prosty sposób przy³±czyæ siê
do tocz±cej siê gry poprzez wskazanie jej w menu.

%prep
%setup -q -a1
cd %{_mserv}
%patch0 -p1

%build
%configure
%{__make}

cd %{_mserv}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{_mserv}/src/bomberclonemserv \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/games/%{name}
%{_includedir}/%{name}

%files master_server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bomberclonemserv
