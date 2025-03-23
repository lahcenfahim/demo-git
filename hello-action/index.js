const core = require('@actions/core');

function run() {
    try {
        const name = core.getInput('name');
        const greeting = core.getInput('greeting');
        const message = `${greeting}, ${name}!`;
        console.log(message);
        core.setOutput("message", message);
    } catch (error) {
        core.setFailed(error.message);
    }
}

run();
