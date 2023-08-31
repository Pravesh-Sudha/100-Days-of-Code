df -H | awk '{print $5 "" $1}' | while read output;
do
echo "Disk Details: ${output}"
usage=$(echo $output | awk '{print $1+0}')
file_sys=$(echo $output | awk '{print $2}')

if [ $usage -ge 90 ]; then
   echo "Critical for ${file_sys}" 
fi 
done
  