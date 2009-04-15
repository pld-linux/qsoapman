Summary:	Qt SOAP Manager
Name:		qsoapman
Version:	0.4
Release:	0.1
License:	GPL
Group:		X11/Applications
URL:		http://qsoapman.sourceforge.net/
Source0:	http://dl.sourceforge.net/qsoapman/%{name}-%{version}.tar.gz
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt SOAP Manager is a GUI tool for sending SOAP messages. It can be
used for the development, debugging or exploration of Web Services. It
is written in C++ and should run on every platform supported by Qt.

%prep
%setup -q
rm -f src/Makefile

%build
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install bin/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO *.xml
%attr(755,root,root) %{_bindir}/%{name}
