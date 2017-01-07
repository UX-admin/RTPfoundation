#
# CDDL HEADER START
#
# The  contents of this file are subject to the terms of the Common
# Development and  Distribution  License,  Version  1.0  only  (the
# "License").  You  may not use this file except in compliance with
# the License.
# 
# A  copy  of  the  Common  Development and Distribution License is
# available at:
# 
# https://github.com/UX-admin/rpmmacros/blob/master/LICENSE
# 
# see the License for the specific language  governing  permissions
# and limitations under the License.
# 
# When  distributing Covered Code, include this CDDL header in each
# file, and include the "LICENSE" file.
# 
# If applicable, add the following below this CDDL header, with the
# fields   enclosed   by  brackets  "[]"  replaced  with  your  own
# identifying  information:  Portions  Copyright  [yyyy]  [name  of
# copyright owner]
#
# CDDL HEADER END
#
Name: RTPfoundation
Summary: Runtime platform file system structure
Version: 2017.01.02
Release: 01%{?dist}
BuildArch: noarch
BuildRoot: %{_topdir}/BUILD/%{name}-root
License: CDDL (common development and distribution license)
Group: System/Base
URL: http://www.securefw.net/
Vendor: RENIX
Packager: RENIX

%if %{redhat}
Requires: filesystem coreutils
%endif
%if %{ubuntu}
Requires: base-files coreutils man-db
%endif

Provides: %{name}-%{version}-%{release} %{name} = %{version}-%{release}
Conflicts: %{name} < %{version}-%{release}

%define RTP_LOGIN root
%define RTP_GROUP root
%define RTP_BASE opt/rtp

%if %{ubuntu}
%define RTP_MAN_LOGIN man
%define RTP_MAN_GROUP root
%endif


%description
%{RTP_BASE},  etc/%{RTP_BASE}  and  var/%{RTP_BASE}  file  system
anchors and underlying structure and file(s). These include  bin,
sbin, share/man, lib, and so on.


%install
#
# All directories are called out for clarity.
#
DirList="%{_prefix} %{_sysconfdir} %{_bindir} %{_sbindir} %{_mandir} %{_includedir} %{_localstatedir} %{_var}/%{RTP_BASE}/lib %{_var}/%{RTP_BASE}/lib/rpm %{_var}/%{RTP_BASE}/cache /%{RTP_BASE}/lib64 /%{RTP_BASE}/lib"

%if %{ubuntu}
DirList="${DirList} %{_var}/%{RTP_BASE}/cache/man"
%endif

for Dir in ${DirList}
do
  %{__mkdir_p} "%{buildroot}${Dir}"
done


%clean
%__rm -rf %{buildroot}/


%files
%defattr(0644 %{RTP_LOGIN} %{RTP_GROUP} 0755)
%attr(0755 %{RTP_LOGIN} %{RTP_GROUP}) %{_prefix}
%attr(0755 %{RTP_LOGIN} %{RTP_GROUP}) %{_sysconfdir}
%dir %{_var}/%{RTP_BASE}
%dir %{_var}/%{RTP_BASE}/lib
%attr(0750 %{RTP_LOGIN} %{RTP_GROUP}) %{_var}/%{RTP_BASE}/lib/rpm
%dir %{_var}/%{RTP_BASE}/cache
%if %{ubuntu}
%attr(2755 %{RTP_MAN_LOGIN} %{RTP_MAN_GROUP}) %{_var}/%{RTP_BASE}/cache/man
%endif
