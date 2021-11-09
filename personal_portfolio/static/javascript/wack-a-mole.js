var score = 0;
var scoreText;
var width = 800;
var height = 600;


var config = {
    type: Phaser.AUTO,
    width: width,
    height: height,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    parent: "my-game",
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);
var timedEvent;

function preload ()
{
    this.load.image('sky', static_url + 'assets/sky.png');
    this.load.image('ground', static_url + 'assets/platform.png');
    this.load.image('star', static_url +
        'assets/star.png',
        { frameWidth: 320, frameHeight: 420 });
    this.load.image('bomb', static_url + 'assets/bomb.png');
    this.load.spritesheet('dude', static_url +
        'assets/dude.png',
        { frameWidth: 32, frameHeight: 48 }
    );
}

var platforms;
var starCount = 0;

function create ()
{
    this.add.image(400, 300, 'sky');
    cursors = this.input.keyboard.createCursorKeys();

    stars = this.physics.add.staticGroup();
    spawnStar()
    scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: '#000' });

    //  Create our Timer

    //  Start the timer running - this is important!
    //  It won't start automatically, allowing you to hook it to button events and the like.

    makeTimer();
}

function makeTimer () {
    var temp = "temp message";

    timedEvent = this.time.addEvent({
        delay: 500,                // ms
        callback: spawnStar,
        args: [temp],
        callbackScope: this,
        loop: true
    });

}

function spawnStar(temp){
    console.log(temp);
    if (starCount <= 5) {
        starCount++;
        var starWidth = Phaser.Math.FloatBetween(0, width);
        var starHeight = Phaser.Math.FloatBetween(0, height);

        var star = stars.create(starWidth, starHeight, 'star');
        star.setScale(5)
        star.setInteractive().on('pointerdown', function(pointer, localX, localY, event){
                collectStar(star);
        });

        //timedEvent = this.time.delayedCall(500, removeStar, [this.star], this);  // delay in ms
    }
}

function test() {
    console.log("test passed!")

}

function update ()
{
}

function collectStar (star)
{
    removeStar();
    score += 10;
    scoreText.setText('Score: ' + score);
}

function removeStar(star){
    star.disableBody(true, true);
    starCount--;
}