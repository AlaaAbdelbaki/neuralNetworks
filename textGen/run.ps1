$types = @("RNN", "LSTM", "GRU")


for ($typeIndex = 0; $typeIndex -lt $types.Length; $typeIndex++) {
    $type = $types[$typeIndex]
    for ($i = 2; $i -le 32; $i = $i * 2) {
        for ($j = 128; $j -le 1024; $j = $j * 2) {
            # Call the python script here
            Write-Output "Running with num_layers=$i and hidden_size=$j and decoder=$type"
            python .\articleGeneration.py --num_layers $i --hidden_size $j --decoder $type
        }
    }
}
