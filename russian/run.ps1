$types = @("RNN", "LSTM", "GRU")

$light = @("true", "false")

Clear-Host;
for ($lightIndex = 0; $lightIndex -lt $light.Length; $lightIndex++) {
    $isLight = $light[$lightIndex]
    for ($i = 1; $i -le 8; $i++) {
        for ($j = 8; $j -le 256; $j = $j * 2) {
            # Call the python script here
            if ($isLight -eq "true") {
                Write-Output "Running with num_layers=$i and hidden_size=$j in light mode"
                python .\nameGeneration_modified.py --num_layers $i --hidden_size $j --light
            }
            else {
                Write-Output "Running with num_layers=$i and hidden_size=$j in full mode"
                python .\nameGeneration_modified.py --num_layers $i --hidden_size $j
            } 
        }
    }
}
