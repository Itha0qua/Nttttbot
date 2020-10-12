from treys import *
evalu = Evaluator()
class texas:
    def init(self):
        self.deck = Deck()
        self.playerlist = {}
        self.board = []


    def new_game(self):
        try:
            self.deck = Deck()
            self.board = self.deck.draw(5)
            self.playerlist = {}
        except:
            return '创建失败'
        else:
            return '创建成功'


    def add_player(self, name):
        if name in self.playerlist:
            return '已经加入了'
        hand = self.deck.draw(2)
        self.playerlist[name] = hand
        return '你的手牌是：' + Card.int_to_pretty_str(hand[0])+' '+Card.int_to_pretty_str(hand[1])


    def remove_player(self , name):
        if name not in self.playerlist:
            return '查无此人'
        else:
            del self.playerlist[name]
            return '弃牌成功'

    def show_board(self,start,end):
        result = '牌桌：\n'
        for i in range(start,end):
            result += Card.int_to_pretty_str(self.board[i])+'\n'
        return result

    def end(self):
        max = float('inf')
        maxi = ''
        for i in self.playerlist:
            tem  = evalu.evaluate(self.playerlist[i],self.board)
            if tem < max:
                max = tem
                maxi = i
        hand = self.playerlist[maxi]
        return '赢家：'+maxi+'\n手牌：'+ Card.int_to_pretty_str(hand[0])+' '\
        +Card.int_to_pretty_str(hand[1])+'\n牌型：'+ evalu.class_to_string(evalu.get_rank_class(max))


if __name__ == '__main__':
    te = texas()
    print(te.new_game())
    print(te.add_player('111'))
    print(te.add_player('111'))
    print(te.add_player('222'))
    print(te.show_board(0,3))
    print(te.show_board(0,4))
    print(te.show_board(0,5))
    print(te.end())
