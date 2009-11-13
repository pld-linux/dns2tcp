Summary:	dns2tcp - relay connections throught DNS traffic
Name:		dns2tcp
Version:	0.4.3
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.hsc.fr/ressources/outils/dns2tcp/download/%{name}-%{version}.tar.gz
# Source0-md5:	d2b322ee27f4ff53dfdad61aa2f42dd8
URL:		http://www.hsc.fr/ressources/outils/dns2tcp/index.html.en
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dns2tcp is a network tool designed to relay TCP connections through
DNS traffic. Encapsulation is done on the TCP level, thus no specific
driver is needed (i.e: TUN/TAP). Dns2tcp client doesn't need to be run
with specific privileges.

Dns2tcp is composed of two parts : a server-side tool and a
client-side tool. The server has a list of resources specified in a
configuration file. Each resource is a local or remote service
listening for TCP connections. The client listen on a predefined TCP
port and relays each incoming connection through DNS to the final
service.

%prep
%setup -q

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/dns2tcpc.1*
%{_mandir}/man1/dns2tcpd.1*
