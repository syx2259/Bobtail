# Bobtail
<h2>
  Instruction
</h2>
<p>For this project, we have set up three different experiments. First we install thrift RPC server.</p>
<h3>
  Requirements
</h3>
Follow the following links to install thrift.
<ul>
  <li>https://thrift.apache.org/docs/install/debian.html</li>
  <li>https://thrift.apache.org/download</li>
  <li>https://thrift-tutorial.readthedocs.io/en/latest/installation.html</li>
</ul>
Then we need to setup 2 VM machines in GCP.
To do...

<h3>
  Instruction for repeat experiments
</h3>
For each experiment, you just need to go to each folder, download client folder to client L1 VM and download
<ol>
  <li>Go to each folder</li>
  <li>Download client folder to client L1 VM</li>
  <li>Download server folder to regular server L2 VM, server_target folder to target server L2 VM</li>
</ol>
To run server:
<ol>
  <li>In server folder, go into server folder</li>
  <li>run `python3 PythonServer.py`</li>
</ol>
To run client:
<ol>
  <li>In server folder, go into client folder</li>
  <li>run <code>python3 PythonClient.py</code></li>
</ol>
