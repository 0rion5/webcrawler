<!DOCTYPE html>
<html>

<head>
    <h1>Simple webcrawler</h1>
</head>

<body>
    <h2 id="section1">Setup</h2>
    <p>
        <h2 id="requirements">Requirements</h2>
        <ul>
            <li>Anaconda Python distribution installed and accessible</li>
        </ul>
        <h2 id="check-conda-is-installed-and-in-your-path">1. Check conda is installed and in your PATH</h2>
        <ol>
            <li>Open a terminal client.</li>
            <li>Enter <code>conda -V</code> into the terminal command line and press enter.</li>
            <li>If conda is installed you should see somehting like the following.</li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash"><span class="nv">$ </span>conda -V 
conda 3.7.0</code></pre></div>
        <h2 id="check-conda-is-up-to-date">2. Check conda is up to date</h2>
        <ol>
            <li>In the terminal client enter</li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash">conda update conda</code></pre></div>
        <ol>
            <li>Upadate any packages if necessary by typing <code>y</code> to proceed.</li>
        </ol>
        <h2 id="create-a-virtual-environment-for-your-project">3. Create a virtual environment for your project</h2>
        <ol>
            <li>In the terminal client enter the following where <em>webcrawlerenv</em> is the name you want to call your environment, and replace <em>x.x</em> with the Python version you wish to use. (To see a list of available python versions first, type <code>conda search "^python$"</code> and press enter.) </li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash">conda create -n webcrawlerenv</code></pre></div>
        <ol>
            <li>Press <code>y</code> to proceed. This will install the Python version and all the associated anaconda packaged libraries at “path_to_your_anaconda_location/anaconda/envs/yourenvname”</li>
        </ol>
        <h2 id="activate-your-virtual-environment">4. Activate your virtual environment.</h2>
        <ol>
            <li>To activate or switch into your virtual environment, simply type the following where <em>webcrawlerenv</em> is the name you gave to your environement at creation.</li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash"><span class="nb">conda </span>activate webcrawlerenv</code></pre></div>
        <ol>
            <li>Activating a conda environment modifies the PATH and shell variables to point to the specific isolated Python set-up you created. The command prompt will change to indicate which conda environemnt you are currently in by prepending <code>(yourenvname)</code>. To see a list of all your environments, use the command <code>conda info -e</code>.</li>
        </ol>
        <h2 id="install-additional-python-packages-to-a-virtual-environment">5. Install additional Python packages to a virtual environment.</h2>
        <ol>
            <li>To install additional packages only to your virtual environment, enter the following command where <em>webcrawlerenv</em> is the name of your environemnt, and <em>[package]</em> is the name of the package you wish to install. <em>Failure to specify “-n webcrawlerenv” will install the package to the root Python installation.</em> </li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash">conda install -n webcrawlerenv <span class="o"></span>selenium, bs4, pandas, matplotlib<span class="o"></span></code></pre></div>
        <h2 id="deactivate-your-virtual-environment">6. Deactivate your virtual environment.</h2>
        <ol>
            <li>To end a session in the current environment, enter the following. There is no need to specify the envname - which ever is currently active will be deactivated, and the PATH and shell variables will be returned to normal.</li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash"><span class="nb">conda </span>deactivate</code></pre></div>
        <h2 id="delete-a-no-longer-needed-virtual-environment">7. Delete a no longer needed virtual environment</h2>
        <ol>
            <li>To delete a conda environment, enter the following, where <em>webcrawlerenv</em> is the name of the environment you wish to delete.</li>
        </ol>
        <div class="highlight"><pre><code class="language-bash" data-lang="bash">conda remove --name webcrawlerenv --all</code></pre></div>
        <h2 id="related-info">Related info</h2>
        <p>The conda offical documentation can be found <a href="http://conda.pydata.org/docs/intro.html">here</a>.</p>
        <h2 id="check-conda-is-installed-and-in-your-path">8. Install Chromedriver</h2>
        <ol>
            <li>Go to https://chromedriver.chromium.org/downloads</li>
            <li>Download the same version as your chrome browser.</li>
            <li>Install the executable to PATH.</li>
        </ol>
</body>

</html>
