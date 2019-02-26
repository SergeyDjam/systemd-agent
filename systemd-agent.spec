%define		debug %nil
%define		debug_package %nil

Name:		systemd-agent
Version:	0.0.1
Release:	1
Summary:	Systemd tcp daemon
License:	GPL
URL:		https://github.com/SergeyDjam/systemd-agent
Source:		%{name}.tar.gz
Group:		System/Configuration/Networking
BuildRequires:	go
Requires:	systemd

%description
Managing systemctl over network

%prep
%setup -qn %{name}

%build
go build -o %{name}

%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sudoers.d
install -Dm0755 %{name} %{buildroot}%{_bindir}
install -Dm0755 %{name}.sudoers %{buildroot}%{_sysconfdir}/sudoers.d/%{name}
install -Dm0755 %{name}.cfg.sample %{buildroot}%{_sysconfdir}/%{name}.cfg
install -Dm0755 %{name}.service %{buildroot}%{_unitdir}

%files
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/sudoers.d/%{name}
%{_sysconfdir}/%{name}.cfg


