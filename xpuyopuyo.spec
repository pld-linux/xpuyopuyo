Summary:	A tetris-like puzzle game for X11
Summary(pl):	Tetrisopodobona gra dla X11
Name:		xpuyopuyo
Version:	0.9.8
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://chaos2.org/xpuyopuyo/%{name}-%{version}.tar.gz
# Source0-md5:	5286312415d632011cfd0e603f55c428
Source1:	%{name}.desktop
Patch0:		%{name}-am_link.patch
URL:		http://chaos2.org/xpuyopuyo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	libmikmod-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xpuyopuyo is a Tetris-like puzzle game where you strive to match up
four ``blobs'' of the same color. Each match gives you points, and
also dumps gray rocks on your opponent which are irritating and
troublesome to get rid of. Multiple matches at one time score more
points, and result in more rocks being dumped on the opponent (much to
their dismay). First person to fill up their screen with puyopuyo
blobs loses.

%description -l pl
Xpuyopuyo to tetrisopodobna gra puzlowa, w której starasz siê ustawiæ
cztery klocki tego samego kolory. Ka¿de dopasowanie daje ci punkty
oraz zrzuca szare ska³y na twojego przeciwnika, który jest irytuj±cy i
ciê¿ko siê go pozbyæ. Wielokrotne dopasowania s± warte wiêcej punktów
i skutkuj± w wiêkszej liczbie ska³ zrzucanych na przeciwnika (na ich
trwogê).

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
