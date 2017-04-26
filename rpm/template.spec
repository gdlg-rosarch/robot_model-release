Name:           ros-lunar-joint-state-publisher
Version:        1.12.9
Release:        0%{?dist}
Summary:        ROS joint_state_publisher package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/joint_state_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-python-qt-binding
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-rostest

%description
This package contains a tool for setting and publishing joint state values for a
given URDF.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Apr 26 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.9-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-2
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-1
- Autogenerated by Bloom

* Mon Apr 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

