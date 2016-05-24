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
	
	function showResults($array, $teamFor, $teamAgainst)
	{
		$complete = FALSE;
		foreach($array as $value)
		{
			if($value['Team One'] == $teamFor)
			{
				if($value['Team Two'] == $teamAgainst)
				{	
					displayResults($value);
					$complete = TRUE;
				}	
			}
		}
		if($complete == FALSE)
			echo "Bad Selection";
	}
	
	function displayResults($value)
	{
		echo "<table class = 'table' style = 'text-align:center; margin: 0 auto;' border='0'>";
		echo "<tr>";
		//echo "<td></td>";
		echo "<td>Home</td>";
		echo "<td>Percent</td>";
		//echo "<td></td>";
		echo "<td>Away</td>";
		echo "</tr>";
		//donut is try at circliful donut graph
		$donut = '<link href="css/jquery.circliful.css" rel="stylesheet" type="text/css" />
				  <script src ="/js/jquery.min.js"></script>
				  <script src = "js/jquery.circliful.min.js"></script>
						<script>
							$( document ).ready(function() {
									$("your-circle").circliful({
										animationStep: 5,
										foregroundBorderWidth: 5,
										backgroundBorderWidth: 15,
										percent:'.$value['Percent'].
									'});
							});
						</script>';
		if($value['Percent'] <= 50)
		{
			
			echo "<tr>";
			echo "<td><img src ='images/CapstoneImages/{$value['Team One']}.png' style = 'opacity:0.4;'>";
			echo "{$value['Team One']}</td>";
			echo "<td>{$value['Percent']}%</td>";
			echo "<td><img src ='images/CapstoneImages/{$value['Team Two']}.png'>";
			echo "{$value['Team Two']}</td>";
			echo '</tr>';
			//echo $donut;
		}
		else
		{
			echo "<tr>";
			echo "<td><img src ='images/CapstoneImages/{$value['Team One']}.png'>";
			echo "{$value['Team One']}</td>";
			echo "<td>{$value['Percent']}%</td>";
			echo "<td><img src ='images/CapstoneImages/{$value['Team Two']}.png' style = 'opacity:0.4;'></td>";
			echo "<td>{$value['Team Two']}</td>";
			echo '</tr>';
		}
	}
	
	$gameData = csv_to_array('final_results_.csv');
	$team_one = $_POST['Home'];
	$team_two = $_POST['Away'];
	showResults($gameData, $team_one, $team_two);
?>