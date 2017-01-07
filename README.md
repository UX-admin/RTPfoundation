###**NAME**
RTPfoundation - Runtime platform file system structure

###**SYNOPSIS**
All the files required to build a System V and RPM packages of the runtime platform foundation.

###**DESCRIPTION**
This repository contains the metadata files required to build the runtime platform SVR4 and RPM packages.

The runtime platform is an architectural abstraction on top of several different operating systems (Solaris, HP-UX, RHEL, and Ubuntu) implemented in software, and providing a set of guaranteed functionality to the consumer of the computing services. The `RTPfoundation` package creates the required filesystem structure on which all other software packages can rely:

* /opt/rtp
* /etc/opt/rtp[/application_name]
* /var/opt/rtp[/application_name]

The above structure is in strict compliance with the following specifications: System V filesystem specification, as documented in the [filesystem(5)](https://illumos.org/man/5/filesystem) manual page, as well as [Linux Standards Base, Filesystem Hierarchy Standard](http://refspecs.linuxfoundation.org/fhs.shtml).

The intent is that no other package may modify the attributes, owner, or the permissions, and that these can be formally verified through the software management subsystem, for example with `pkgchk -v RTPfoundation`, respectively `rpm -V RTPfoundation`, the goal being to:

* provide a guaranteed filesystem state to applications;
* ensure applications are packaged correctly;
* ensure that no manual tampering with the system took place.

###**BUILDING THE SOFTWARE**
####**SOLARIS-BASED SYSTEMS**
This section covers any Solaris-based system which utilizes
[AT&T System V](https://en.wikipedia.org/wiki/UNIX_System_V)
packaging, ranging from Solaris 10 to
[illumos](https://wiki.illumos.org/display/illumos/About+illumos)-based systems
like [Tribblix](http://tribblix.org/).

1. `mkdir -p ${HOME}/repos && cd ${HOME}/repos/`

2. `git pull https://github.com/UX-admin/RTPfoundation/ && cd RTPfoundation`

3. `pkgmk -of prototype.`uname -p``; the package will be built in
   `/var/spool/pkg/` by default.

4. become superuser or assume the equivalent privilege, for example with sudo or
   with **[pfexec(1)](https://illumos.org/man/1/pfexec)**:

   ```
   % su -
   Password:
   # yes | pkgadd RTPfoundation
   # exit
   ```

   ```Tcsh
   % yes | sudo pkgadd RTPfoundation
   ```

####**RPM-BASED SYSTEMS**
This section covers any RPM-based system, ranging from redhat Enterprise Linux (RHEL) to Atari ST MiNT.

1. `mkdir -p ${HOME}/repos && cd ${HOME}/repos/`

2. `git pull https://github.com/UX-admin/rpmmacros/`

3. install the `rpmmacros` file as `/etc/rpmmacros`, or as `${HOME}/.rpmmacros`;
   if you choose to install it as `/etc/rpmmacros`, you should package it first
   so no manual modifications are made to the system, otherwise
   `cp rpmmacros/.rpmmacros $HOME`.

4. `git pull https://github.com/UX-admin/RTPfoundation/`

5. install the package containing the
   **[rpmbuild(8)](https://linux.die.net/man/8/rpmbuild)** program; depending on
   the operating system, this package might be called `rpmbuild` or `rpm-build`:

   ```
   % su -
   Password:
   # yum install -y rpm-build
   # exit
   ```

   or alternatively:

   ```
   % sudo yum install -y rpm-build
   ```

6. create the RPM build structure.

   (Bourne shell family:)
   
   ```shell
   $ for Directory in BUILD BUILDROOT RPMS/`uname -p` RPMS/noarch SOURCES SPECS SRPMS
   do
     mkdir -p ${HOME}/devel/rpms/${Directory}
   done
   ```
   
   (C-shell family:)
   
   ```Tcsh
   % foreach Directory (BUILD BUILDROOT RPMS/`uname -p` RPMS/noarch SOURCES SPECS SRPMS)
      mkdir -p ${HOME}/devel/rpms/${Directory}
   end
   ```

7. `rpmbuild --clean -ba RTPfoundation/SPECS/RTPfoundation.spec`

   the binary RPM package will be generated in
   `${HOME}/devel/rpms/RPMS/noarch/`, and the source RPM in
   `${HOME}/devel/rpms/SRPMS/`. The `.src.rpm` (SRPM) package encapsulates
   everything needed to modify and rebuild the binary package again.

8. install the package with **[sudo(8)](https://linux.die.net/man/8/sudo)**:

   ```Tcsh
   % sudo rpm -Uvh ${HOME}/devel/rpms/RPMS/noarch/RTPfoundation-2017.01.02-01.noarch.rpm
   ```
   
   or alternatively, become superuser, and then install the package:

   ```
   % su -
   Password:
   # rpm -Uvh /export/home/buildusr/devel/rpms/RPMS/noarch/RTPfoundation-2017.01.02-01.noarch.rpm
   # exit
   %
   ```
