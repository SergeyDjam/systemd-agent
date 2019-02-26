Name:		systemd-agent
Version:	0.0.1
Release:	1
Summary:	Systemd tcp daemon
License:	GPL
Source:		%{name}-%{version}.tar.gz
Group:		System
BuildRequires:	go
Requires:	systemd

%description
Managing systemctl over network

%prep
%setup -q %{name}-%{version}

%build
go build -o %{name}

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sudoers.d
install -Dm0755 %{name} %{buildroot}%{_bindir}
install -Dm0755 %{name}.sudoers %{buildroot}%{_sysconfdir}/suders.d/%{name}
install -Dm0755 %{name}.cfg.sample %{buildroot}%{_sysconfdir}/%{name}.cfg

%files
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/sudoers.d/%{name}
%{_sysconfdir}/%{name}.cfg


