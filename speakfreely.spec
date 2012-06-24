%define		ver 7.5
%define		xspeakfreely_ver 0.8.1.b
Summary:	Speak Freely - network voice phone
Summary(pl.UTF-8):   Speak Freely - internetowy telefon
Summary(pt_BR.UTF-8):   Cliente para telefonia via Internet com suporte ao protocolo RTP
Name:		speakfreely
Version:	%{ver}
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/speak-freely-u/speak_freely-%{version}.tar.gz
# Source0-md5:	fd315f8fd9996b7f34e83d8249ecd89f
Patch0:		speak_freely-Makefile.patch
Patch1:		speak_freely-xspeakfree-FHS.patch
Patch2:		speak_freely-xspeakfree-pidfiles.patch
Patch3:		speak_freely-system-libgsm.patch
URL:		http://www.fourmilab.ch/speakfree/unix/
BuildRequires:	libgsm-devel >= 1.0.2
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speak Freely is a application for a variety of Unix workstations that
allows you to talk (actually send voice, not typed characters) over a
network. If your network connection isn't fast enough to support
real-time voice data, various forms of compression may allow you,
assuming your computer is fast enough, to converse nonetheless. To
enable secure communications, encryption with DES, Blowfish, IDEA,
and/or a key file is available. If PGP is installed on the user's
machine, it can be invoked automatically to exchange IDEA session keys
for a given conversation. Speak Freely for Unix is compatible with
Speak Freely for Windows, and users of the two programs can
intercommunicate.

%description -l pl.UTF-8
Speak Freely pozwala rozmawiać przez sieć z wieloma osobami na raz, w
przypadku kart dźwiękowych full-duplex umożliwiając jednoczesne
odbieranie i nadawanie dźwięku. Program zna kilka rodzajów kompresji,
co umożliwia jego zastosowania również w wolniejszych sieciach, które
nie są w stanie zapewnić przesyłania pełnego sygnału audio w czasie
rzeczywistym. Możliwe jest szyfrowanie transmisji za pomocą jednego z
algorytmów DES, Blowfish, IDEA. Za pomocą Speak Freely można
komunikować się również z użytkownikami Speak Freely for Windows
(http://www.fourmilab.ch/speakfree/windows/).

Program uruchamia się poleceniem 'sflaunch' (lub można osobno
uruchomić program odbiornika 'sfspeaker &' i program nadajnika 'sfmike
<hostname>'.

UWAGA: Wersja binarne została skompilowana w full-duplex. Jeśli Twoja
karta lub sterownik do niej nie obsługują full-duplex, trzeba
przekompilować pakiet z włączoną opcją half-duplex (opisane jest to w
Makefile).

%description -l pt_BR.UTF-8
O Speak Freely permite que duas máquinas possam ser usadas para
transmissão de voz sobre TCP/IP. Suporte compressão, criptografia e o
protocolo RTP.

%package -n xspeakfree
Summary:	GUI to Speak Freely
Summary(pl.UTF-8):   Graficzny interfejs użytkownika dla Speak Freely
Version:	%{xspeakfreely_ver}
Group:		Applications/Communications
Requires:	%{name} = %{ver}-%{release}

%description -n xspeakfree
This is Tk-based GUI for Speak Freely.

%description -n xspeakfree -l pl.UTF-8
Ten pakiet zawiera oparty o Tk graficzny interfejs do Speak Freely.

%prep
%setup -q -n speak_freely-%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	INSTDIR=%{_prefix} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags} -Wall -DHEXDUMP" \
%ifarch ppc sparc sparc64 sparcv9
	ENDIAN="BIG"
%else
	ENDIAN="LITTLE"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	INSTDIR="$RPM_BUILD_ROOT%{_prefix}"

install -d $RPM_BUILD_ROOT%{_datadir}/xspeakfree
install CONTRIB/xspeakfree-0.8.1.b/bin/* $RPM_BUILD_ROOT%{_bindir}
install CONTRIB/xspeakfree-0.8.1.b/lib/xspeakfree/* $RPM_BUILD_ROOT%{_datadir}/xspeakfree

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/sf*
%{_mandir}/man1/sf*.1*

%files -n xspeakfree
%defattr(644,root,root,755)
%doc CONTRIB/xspeakfree-0.8.1.b/{BUGS,HISTORY,LICENSE,README,TODO}
%doc CONTRIB/xspeakfree-0.8.1.b/xspeakfree-help.html
%attr(755,root,root) %{_bindir}/xspeakfree
%{_datadir}/xspeakfree*
