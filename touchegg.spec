Summary:	Touchegg - Multitouch gesture recognizer
Summary(en.UTF-8):	Touchégg - Multitouch gesture recognizer
Name:		touchegg
Version:	1.1.1
Release:	2
License:	GPL v3
Group:		Applications
Source0:	https://touchegg.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	60cf15a541bd52c15be84950f8e88d1f
URL:		http://code.google.com/p/touchegg/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	geis-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Touchegg - Multitouch gesture recognizer.

%description -l en.UTF-8
Touchégg - Multitouch gesture recognizer.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/touchegg
%dir %{_datadir}/touchegg
%{_datadir}/touchegg/touchegg.conf
