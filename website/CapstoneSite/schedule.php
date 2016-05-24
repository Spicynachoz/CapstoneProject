<?php
	header('Content=Type:text/xml');
	echo '<?xml version="1.0" encoding="UTF=8" standalone="yes" ?>';
	
	function csv_to_array($filename='', $delimiter=',')
	{
		if(!file_exists($filename) || !is_readable($filename))
		return FALSE;
	
		$header = NULL;
		$data = array();
		if (($handle = fopen($filename, 'r')) !== FALSE)
		{
			while (($row = fgetcsv($handle, 1000, $delimiter)) !== FALSE)
			{
				if(!$header)
					$header = $row;
				else
					$data[] = array_combine($header, $row);
			}
		fclose($handle);
		}
		return $data;
	}
			
	function printTable($value)
	{
		echo '<tr>'; 
		echo "<td>{$value['Date']}</td>";
		echo "<td><img src='images/CapstoneImages/{$value['Visitor']}.png'></td>";
		echo "<td id = 'Away' >{$value['Visitor']}</td>";
		echo "<td>{$value['PTS Away']}</td>	";
		echo "<td><img src='images/CapstoneImages/{$value['Home']}.png'></td>";
		echo "<td id= 'Home'>{$value['Home']}</td>";
		echo "<td>{$value['PTS Home']}</td>";
		echo '</tr>';
	}	
	function showSchedule($array, $month, $teamName)
	{
		/*$exists = FALSE;
		foreach($array as $value)
		{	
			if($month!= 'NULL')
				if($teamName !== 'NULL')
					if($value['Visitor'] == $teamName || $value['Home'] == $teamName)
						$exists = TRUE;
					else
					{
					 
					}
				else
					$exists = TRUE;
		}
		if($exists == TRUE)
		{*/
			echo '<table class = "table" style = "text-align:center; margin: 0 auto;" border="1">';
			echo '<tr>';
			echo "<td>Date</td>";
			echo "<td>Logo</td>"
;			echo "<td>Visitor</td>";
			echo "<td>PTS Away</td>";
			echo "<td>Logo</td>";
			echo "<td>Home</td>";
			echo "<td>PTS Home</td>";	
			foreach($array as $value)
			{	
				if($month != 'NULL')
				{
					if(strpos($value['Date'],$month) !== False)
					{
						if($teamName !== 'NULL')
						{
							if($value['Visitor'] == $teamName)
								printTable($value);
							else if($value['Home'] == $teamName)
								printTable($value);
						}
						else
							if(strpos($value['Visitor'],$month) !== False);
							else
								printTable($value);
					}
				}			
				else
					if($value['Visitor'] == $teamName)
					{
						printTable($value);
					}
					else if($value['Home'] == $teamName)
					{
						printTable($value);
					}
			}
			echo '</table>';
		//}

	}
	
	$teamName = $_POST['Team'];
	$month = $_POST['Month'];
	if($month == 'Playoffs')
	{
		$Playoffs = csv_to_array('playoff.csv');
		showSchedule($Playoffs, 'NULL', $teamName);
	}
	else
	{
		$NBASchdule = csv_to_array('NBASchedule.csv');	
		showSchedule($NBASchdule, $month, $teamName);
	}
?>