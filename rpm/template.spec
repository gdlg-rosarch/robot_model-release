Name:           ros-indigo-collada-urdf
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS collada_urdf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       collada-dom-devel
Requires:       ros-indigo-angles
Requires:       ros-indigo-collada-parser
Requires:       ros-indigo-geometric-shapes
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  assimp-devel
BuildRequires:  collada-dom-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-collada-parser
BuildRequires:  ros-indigo-geometric-shapes
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel

%description
This package contains a tool to convert Unified Robot Description Format (URDF)
documents into COLLAborative Design Activity (COLLADA) documents. Implements
robot-specific COLLADA extensions as defined by
http://openrave.programmingvision.com/index.php/Started:COLLADA

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 27 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Wed Jan 04 2017 Ioan Sucan <isucan@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

* Fri Jun 10 2016 Ioan Sucan <isucan@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Tue Feb 23 2016 Ioan Sucan <isucan@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Ioan Sucan <isucan@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Fri Sep 11 2015 Ioan Sucan <isucan@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Ioan Sucan <isucan@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Sun Nov 30 2014 Ioan Sucan <isucan@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu Jul 24 2014 Ioan Sucan <isucan@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

