Name:           ros-indigo-collada-parser
Version:        1.11.7
Release:        0%{?dist}
Summary:        ROS collada_parser package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_parser
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       ros-indigo-class-loader
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-urdf-parser-plugin
Requires:       urdfdom-headers-devel
BuildRequires:  collada-dom-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-class-loader
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-urdf-parser-plugin
BuildRequires:  urdfdom-headers-devel

%description
This package contains a C++ parser for the Collada robot description format. The
parser reads a Collada XML robot description, and creates a C++ URDF model.
Although it is possible to directly use this parser when working with Collada
robot descriptions, the preferred user API is found in the urdf package.

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
* Wed Apr 22 2015 Ioan Sucan <isucan@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Sun Nov 30 2014 Ioan Sucan <isucan@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu Jul 24 2014 Ioan Sucan <isucan@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

