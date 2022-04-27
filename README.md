# Bobtail
<h2>
  Instruction
</h2>
<p>For this project, we have set up three different experiments. First, we need to set up 1 L1 VM and 5 L2 VMs within it. Then we need to install thrift RPC server on every single L2 VM. Besides, we need a client machine as well, you have to make sure the client machine is in the same network.</p>
<h3>
  Requirements
</h3>
First we need to setup 2 VM machines in GCP. Following the instructions below.
<ul>
  <li>Create L1 VM: https://cloud.google.com/compute/docs/instances/nested-virtualization/enabling</li>
  <li>Create L2 VM: https://cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms</li>
</ul>
Then follow the following links to install thrift in All L2 server machine and L1 client machine.
<ul>
  <li>https://thrift.apache.org/docs/install/debian.html</li>
  <li>https://thrift.apache.org/download</li>
  <li>https://thrift-tutorial.readthedocs.io/en/latest/installation.html</li>
</ul>




<h4>Note</h4>
<b>If you can't download the L2 VM images in the document above, you can instead download <a href="https://cloud.debian.org/images/cloud/bullseye/latest/debian-11-generic-amd64.qcow2">this</a>.</b>
<br>
<b>Because the default username/password is unknown, you can use <a href="https://freelinuxtutorials.com/fixing-kvm-guest-virsh-console-hangs-at-escape-character/">Guestfish</a> to reset the password.</b>

<h3>
  Instruction for repeat experiments
</h3>
For each experiment:
<ol>
  <li>Go to each folder</li>
  <li>Download client folder to client L1 VM</li>
  <li>Download server folder to regular server L2 VM, server_target folder to target server L2 VM</li>
</ol>
To run server:
<ol>
  <li>In server folder, go into server folder</li>
  <li>run <code>python3 PythonServer.py</code></li>
</ol>
To run client:
<ol>
  <li>In server folder, go into client folder</li>
  <li>run <code>python3 PythonClient.py</code></li>
</ol>
