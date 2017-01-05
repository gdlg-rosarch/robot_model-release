Name:           ros-jade-kdl-parser-py
Version:        1.11.12
Release:        0%{?dist}
Summary:        ROS kdl_parser_py package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kdl_parser_py
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-orocos-kdl >= 1.3.0
Requires:       ros-jade-python-orocos-kdl
Requires:       ros-jade-urdf
Requires:       ros-jade-urdfdom-py
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-orocos-kdl >= 1.3.0
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-urdf

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Jan 04 2017 Jackie Kay <jackie@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Fri Jun 10 2016 Jackie Kay <jackie@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Tue Feb 23 2016 Jackie Kay <jackie@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Jackie Kay <jackie@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

