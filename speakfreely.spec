Summary:	Speak Freely - network voice phone
Summary(pl):	Speak Freely - internetowy telefon
Name:		speakfreely
Version:	7.2
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://www.fourmilab.ch/speakfree/unix/speak_freely-%{version}.tar.gz
Patch0:		speak_freely-Makefile.patch
URL:		http://www.fourmilab.ch/speakfree/unix/
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

%prep
%setup -q -n speak_freely-%{version}
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install sfecho sflaunch sflwl sflwld sfmike sfreflect sfspeaker sfvod \
	$RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
