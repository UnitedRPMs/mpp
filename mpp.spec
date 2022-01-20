%define _legacy_common_support 1
%define debug_package %{nil}
%global _hardened_build 1

%global commit0 786b79f9767d24bed618be60046546b508f9190e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}


# Reduce compression level and build time
%define _source_payload w5.gzdio
%define _binary_payload w5.gzdio

%global _build_id_links none
%undefine __brp_check_rpaths
%global __brp_check_rpaths %{nil}


Name: mpp
Summary: Rockchip Media Process Platform 
Version: 1.5.0
Release: 1%{?dist}
URL: https://github.com/rockchip-linux/mpp/
Group: System Environment/Libraries
Source0: https://github.com/rockchip-linux/mpp/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
License: BSD
BuildRequires: cmake
BuildRequires: gcc-c++
Requires: librockchip-mpp = %{version}-%{release}
Requires: librockchip-vpu = %{version}-%{release}

%description
Chromium Embedded Framework minimal release.

%package        -n librockchip-mpp
Summary:        Libraries for Rockchip Media Process Platform 


%description    -n librockchip-mpp
Libraries for Rockchip Media Process Platform

%package     -n librockchip-vpu
Summary:        Libraries vpu for Rockchip Media Process Platform 

%description -n librockchip-vpu
Libraries vpu for Rockchip Media Process Platform

%package        -n librockchip-devel
Summary:        Development package for %{name}
Requires:       mpp = %{version}-%{release}

%description    -n librockchip-devel
Rockchip Media Process Platform 
This package contains development files for %{name}

%package        -n librockchip-vpu-devel
Summary:        Development package for %{name}
Requires:       mpp = %{version}-%{release}

%description    -n librockchip-vpu-devel
Rockchip Media Process Platform 
This package contains development files for vpu %{name}

%prep
%autosetup -n mpp-%{commit0} -p1

%build
    cmake -B build -DCMAKE_INSTALL_PREFIX="/usr" \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DOBS_MULTIARCH_SUFFIX="%(echo %{_lib} | sed -e 's/lib//')" \
	-DCMAKE_AR=%{_bindir}/gcc-ar \
	-DCMAKE_RANLIB=%{_bindir}/gcc-ranlib \
	-DCMAKE_NM=%{_bindir}/gcc-nm \
	-DUNIX_STRUCTURE=ON \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_VERBOSE_MAKEFILE=OFF \
        -DAVSD_TEST:BOOL='OFF' \
        -DH264D_TEST:BOOL='OFF' \
        -DH265D_TEST:BOOL='OFF' \
        -DJPEGD_TEST:BOOL='OFF' \
        -DMPI_DEC_TEST:BOOL='OFF' \
        -DMPI_ENC_TEST:BOOL='OFF' \
        -DMPI_RC2_TEST:BOOL='OFF' \
        -DMPI_RC_TEST:BOOL='OFF' \
        -DMPI_TEST:BOOL='OFF' \
        -DMPP_BUFFER_TEST:BOOL='OFF' \
        -DMPP_ENV_TEST:BOOL='OFF' \
        -DMPP_INFO_TEST:BOOL='OFF' \
        -DMPP_LOG_TEST:BOOL='OFF' \
        -DMPP_MEM_TEST:BOOL='OFF' \
        -DMPP_PACKET_TEST:BOOL='OFF' \
        -DMPP_PLATFORM_TEST:BOOL='OFF' \
        -DMPP_TASK_TEST:BOOL='OFF' \
        -DMPP_THREAD_TEST:BOOL='OFF' \
        -DRKPLATFORM:BOOL='ON' \
        -DVP9D_TEST:BOOL='OFF' \
        -DVPU_API_TEST:BOOL='OFF' \
        -DHAVE_DRM:BOOL='ON' \
        -Wno-dev
   
   %make_build -C build
   
%install
   %make_install -C build

%files
%{_bindir}/mpi_dec_mt_test
%{_bindir}/mpi_dec_multi_test
%{_bindir}/mpi_enc_multi_test
   
%files -n librockchip-mpp
%{_libdir}/librockchip_mpp.so.0
%{_libdir}/librockchip_mpp.so.1
   
%files  -n librockchip-vpu
%{_libdir}/librockchip_vpu.so.0
%{_libdir}/librockchip_vpu.so.1
   
%files -n librockchip-devel
%{_includedir}/rockchip/mpp_buffer.h
%{_includedir}/rockchip/mpp_err.h
%{_includedir}/rockchip/mpp_frame.h
%{_includedir}/rockchip/mpp_meta.h
%{_includedir}/rockchip/mpp_packet.h
%{_includedir}/rockchip/mpp_rc_api.h
%{_includedir}/rockchip/mpp_rc_defs.h
%{_includedir}/rockchip/mpp_task.h
%{_includedir}/rockchip/rk_mpi.h
%{_includedir}/rockchip/rk_mpi_cmd.h
%{_includedir}/rockchip/rk_type.h
%{_includedir}/rockchip/rk_vdec_cfg.h
%{_includedir}/rockchip/rk_vdec_cmd.h
%{_includedir}/rockchip/rk_venc_cfg.h
%{_includedir}/rockchip/rk_venc_cmd.h
%{_includedir}/rockchip/rk_venc_rc.h
%{_includedir}/rockchip/rk_venc_ref.h
%{_libdir}/librockchip_mpp.so
%{_libdir}/pkgconfig/rockchip_mpp.pc
   
%files -n librockchip-vpu-devel
%{_includedir}/rockchip/vpu.h
%{_includedir}/rockchip/vpu_api.h
%{_libdir}/librockchip_vpu.so
%{_libdir}/pkgconfig/rockchip_vpu.pc


%changelog

* Fri Dec 31 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.5.0-1 
- initial RPM
