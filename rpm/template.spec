Name:           ros-kinetic-kdl-parser-py
Version:        1.12.1
Release:        1%{?dist}
Summary:        ROS kdl_parser_py package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kdl_parser_py
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-orocos-kdl >= 1.3.0
Requires:       ros-kinetic-python-orocos-kdl
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-urdfdom-py
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-orocos-kdl >= 1.3.0
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-urdf

%description
The Kinematics and Dynamics Library (KDL) defines a tree structure to represent
the kinematic and dynamic parameters of a robot mechanism. kdl_parser_py
provides Python tools to construct a KDL tree from an XML robot representation
in URDF.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Apr 10 2016 Jackie Kay <jackie@osrfoundation.org> - 1.12.1-1
- Autogenerated by Bloom

* Sun Apr 10 2016 Jackie Kay <jackie@osrfoundation.org> - 1.12.1-0
- Autogenerated by Bloom

* Mon Apr 04 2016 Jackie Kay <jackie@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

