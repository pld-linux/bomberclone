Summary:	Clone of the game AtomicBomberMan
Summary(pl):	Klon gry AtomicBomberMan
Name:		bomberclone
Version:	0.11.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	4ba700b22bf704b15a4e8db38054e1d0
#Source1:	%{name}.desktop
URL:		http://www.bomberclone.de/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clone of the game AtomicBomberMan. It supports multiplayer over the
Internet. 

%description -l pl
Klon gry AtomicBomberMan wspieraj±cy grê z kilkoma graczami w
Internecie. 

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_includedir}/%{name}
