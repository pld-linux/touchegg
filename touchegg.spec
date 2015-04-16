Summary:	Touchégg - Multitouch gesture recognizer
Name:		touchegg
Version:	1.1.1
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	https://touchegg.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	60cf15a541bd52c15be84950f8e88d1f
URL:		http://code.google.com/p/touchegg/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXML-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Touchégg - Multitouch gesture recognizer.

%prep
%setup -q

%build
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGES ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/%{name}*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
