Name:		python-proton-vpn-local-agent
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
%autosetup -n local-agent-rs-1.4.5 -p1
cd python-proton-vpn-local-agent
# tar -zxf %{SOURCE1}
# mkdir -p python-proton-vpn-local-agent/.cargo
# cat >> python-proton-vpn-local-agent/.cargo/config.toml << EOF
# [source.crates-io]
# replace-with = "vendored-sources"

# [source.vendored-sources]
# directory = "vendor"
# EOF

%build
cd python-proton-vpn-local-agent
cargo build --release
# --offline

%files
11
