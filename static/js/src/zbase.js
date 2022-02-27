export class AcGame{
    constructor(id) {
        this.id = id;
        this.$ac_game = $('#' + id);
        this.menu = new AcGameMenu(this);   //创建菜单对象
        this.playground = new AcGamePlayground(this);   //创建Playground对象

        this.start();   //构造函数的延伸
    }


    start() {
    }
}
