%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rmf-fleet-adapter
Version:        1.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmf_fleet_adapter package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-components
Requires:       ros-rolling-rmf-battery
Requires:       ros-rolling-rmf-dispenser-msgs
Requires:       ros-rolling-rmf-door-msgs
Requires:       ros-rolling-rmf-fleet-msgs
Requires:       ros-rolling-rmf-ingestor-msgs
Requires:       ros-rolling-rmf-lift-msgs
Requires:       ros-rolling-rmf-task
Requires:       ros-rolling-rmf-task-msgs
Requires:       ros-rolling-rmf-traffic
Requires:       ros-rolling-rmf-traffic-ros2
Requires:       ros-rolling-rmf-utils
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-catch2
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-components
BuildRequires:  ros-rolling-rmf-battery
BuildRequires:  ros-rolling-rmf-cmake-uncrustify
BuildRequires:  ros-rolling-rmf-dispenser-msgs
BuildRequires:  ros-rolling-rmf-door-msgs
BuildRequires:  ros-rolling-rmf-fleet-msgs
BuildRequires:  ros-rolling-rmf-ingestor-msgs
BuildRequires:  ros-rolling-rmf-lift-msgs
BuildRequires:  ros-rolling-rmf-task
BuildRequires:  ros-rolling-rmf-task-msgs
BuildRequires:  ros-rolling-rmf-traffic
BuildRequires:  ros-rolling-rmf-traffic-ros2
BuildRequires:  ros-rolling-rmf-utils
BuildRequires:  ros-rolling-std-msgs
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Fleet Adapter package for RMF fleets.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Sep 06 2021 Grey <grey@openrobotics.org> - 1.4.0-1
- Autogenerated by Bloom

* Tue Jul 20 2021 Grey <grey@openrobotics.org> - 1.3.0-6
- Autogenerated by Bloom

* Mon Jul 19 2021 Grey <grey@openrobotics.org> - 1.3.0-5
- Autogenerated by Bloom

* Wed Jul 07 2021 Grey <grey@openrobotics.org> - 1.3.0-4
- Autogenerated by Bloom

* Mon Jun 28 2021 Grey <grey@openrobotics.org> - 1.3.0-3
- Autogenerated by Bloom

* Tue Jun 15 2021 Grey <grey@openrobotics.org> - 1.3.0-2
- Autogenerated by Bloom

* Tue Jun 08 2021 Grey <grey@openrobotics.org> - 1.3.0-1
- Autogenerated by Bloom

