Name:           ros-kinetic-collada-urdf
Version:        1.12.0
Release:        0%{?dist}
Summary:        ROS collada_urdf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       collada-dom-devel
Requires:       ros-kinetic-angles
Requires:       ros-kinetic-collada-parser
Requires:       ros-kinetic-geometric-shapes
Requires:       ros-kinetic-resource-retriever
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
BuildRequires:  assimp-devel
BuildRequires:  collada-dom-devel
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-collada-parser
BuildRequires:  ros-kinetic-geometric-shapes
BuildRequires:  ros-kinetic-resource-retriever
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf
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
* Mon Apr 04 2016 Ioan Sucan <isucan@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

* Mon Apr 04 2016 Ioan Sucan <isucan@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

