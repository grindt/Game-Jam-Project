<style>
    table, tr, td{border: none}
    .firstcol {white-space: nowrap; text-align: top; font-weight: bold}
    .other {font-weight: normal}
</style>

# Game Jam Level Editor

<p>On launch, there will be a prompt to enter a filename. If the file exists, then it will open it, if it doesn't it will make a new one.</p>
<p>In the window title, you can see the current file you are working on as well as the amount of player health currently set for the map.</p>

# Controls

<table>
    <tr>
        <th class = firstcol>ESC</th>
        <th class = other>Closes the current pygame window.</th>
    </tr>
    <tr>
        <th class = firstcol>CTRL + N</th>
        <th class = other>This is the same state the editor opens in. Here you just enter a file and if the file exists it loads that file. If it doesn't it creates a new file and loads it.</th>
    </tr>
    <tr>
        <th class = firstcol>CTRL + S</th>
        <th class = other>This saves the file by writing the current game map to a file. In the textbox, you enter the amount of health you want the player to have. If the textbox is left blank, it uses the already existing health value (defaults to 100).</th>
    </tr>
    <tr>
        <th class = firstcol>LMB</th>
        <th class = other>Sets the celltype to wall. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>SHIFT + LMB</th>
        <th class = other>Sets the celltype to floor. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>P + LMB</th>
        <th class = other>Sets the celltype to player. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>E + LMB</th>
        <th class = other>Sets the celltype to enemy. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>B + LMB</th>
        <th class = other>Sets the celltype to boss. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>H + LMB</th>
        <th class = other>Sets the celltype to health. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>D + LMB</th>
        <th class = other>Sets the celltype to door. (Can be held)</th>
    </tr>
    <tr>
        <th class = firstcol>RMB</th>
        <th class = other>Sets the celltype to void. (Can be held)</th>
    </tr>
</table>


# Things to Note
- Files are not automatically saved
- There is no undo/redo