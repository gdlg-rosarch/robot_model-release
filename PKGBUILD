# Script generated with Bloom
pkgdesc="ROS - <tt>robot_model</tt> contains packages for modeling various aspects of robot information, specified in the Xml Robot Description Format (URDF). The core package of this stack is <a href="http://ros.org/wiki/urdf">urdf</a>, which parses URDF files, and constructs an object model (C++) of the robot."
url='http://ros.org/wiki/robot_model'

pkgname='ros-lunar-robot-model'
pkgver='1.12.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-collada-parser'
'ros-lunar-collada-urdf'
'ros-lunar-joint-state-publisher'
'ros-lunar-kdl-parser'
'ros-lunar-resource-retriever'
'ros-lunar-urdf'
'ros-lunar-urdf-parser-plugin'
'urdfdom'
)

conflicts=()
replaces=()

_dir=robot_model
source=()
md5sums=()

prepare() {
    cp -R $startdir/robot_model $srcdir/robot_model
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

