source labs/lab_1/install/setup.sh
(gz sim labs/lab_1/my_fuel_lab/worlds/myworld.sdf 2>/dev/null ) &
sh ./labs/lab_1/my_fuel_lab/scripts/bridge.sh &
xterm ./labs/lab_1/my_fuel_lab/scripts/run_3m_cmd.sh

