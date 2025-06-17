Name:		local-agent-rs
Version:	1.4.5
Release:	1
Source0:	https://github.com/ProtonVPN/local-agent-rs/archive/refs/tags/%{version}.tar.gz
# Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Proton VPN local agent written in Rust
URL:		https://github.com/ProtonVPN/local-agent-rs
License:	GPL
Group:		??
BuildRequires:	cargo

%description

%prep
%autosetup -p1
cd local_agent_rs
# tar -zxf %{SOURCE1}
# mkdir -p local_agent_rs/.cargo
# cat >> local_agent_rs/.cargo/config.toml << EOF
# [source.crates-io]
# replace-with = "vendored-sources"

# [source.vendored-sources]
# directory = "vendor"
# EOF

%build
cd local_agent_rs
cargo build --release
# --offline

%files
11
