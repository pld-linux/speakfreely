%define		ver 7.5
%define		xspeakfreely_ver 0.8.1.b
Summary:	Speak Freely - network voice phone
Summary(pl):	Speak Freely - internetowy telefon
Summary(pt_BR):	Cliente para telefonia via Internet com suporte ao protocolo RTP
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

%description -l pl
Speak Freely pozwala rozmawia� przez sie� z wieloma osobami na raz, w
przypadku kart d�wi�kowych full-duplex umo�liwiaj�c jednoczesne
odbieranie i nadawanie d�wi�ku. Program zna kilka rodzaj�w kompresji,
co umo�liwia jego zastosowania r�wnie� w wolniejszych sieciach, kt�re
nie s� w stanie zapewni� przesy�ania pe�nego sygna�u audio w czasie
rzeczywistym. Mo�liwe jest szyfrowanie transmisji za pomoc� jednego z
algorytm�w DES, Blowfish, IDEA. Za pomoc� Speak Freely mo�na
komunikowa� si� r�wnie� z u�ytkownikami Speak Freely for Windows
(http://www.fourmilab.ch/speakfree/windows/).

Program uruchamia si� poleceniem 'sflaunch' (lub mo�na osobno
uruchomi� program odbiornika 'sfspeaker &' i program nadajnika 'sfmike
<hostname>'.

UWAGA: Wersja binarne zosta�a skompilowana w full-duplex. Je�li Twoja
karta lub sterownik do niej nie obs�uguj� full-duplex, trzeba
przekompilowa� pakiet z w��czon� opcj� half-duplex (opisane jest to w
Makefile).

%description -l pt_BR
O Speak Freely permite que duas m�quinas possam ser usadas para
transmiss�o de voz sobre TCP/IP. Suporte compress�o, criptografia e o
protocolo RTP.

%package -n xspeakfree
Summary:	GUI to Speak Freely
Summary(pl):	Graficzny interfejs u�ytkownika dla Speak Freely
Version:	%{xspeakfreely_ver}
Group:		Applications/Communications
Requires:	%{name} = %{ver}-%{release}

%description -n xspeakfree
This is Tk-based GUI for Speak Freely.

%description -n xspeakfree -l pl
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
