namespace AaaaBbbbCccc {

    public class AaaaBbbbCcccEntityBuilder {

        private sbyte eeeeFfffGggg;

        private short iiiiJjjjKkkk;

        private int mmmmNnnnOooo;

        public sbyte EeeeFfffGggg() {
            return this.eeeeFfffGggg;
        }

        public short IiiiJjjjKkkk() {
            return this.iiiiJjjjKkkk;
        }

        public int MmmmNnnnOooo() {
            return this.mmmmNnnnOooo;
        }

        public AaaaBbbbCcccEntityBuilder(sbyte eeeeFfffGggg, short iiiiJjjjKkkk, int mmmmNnnnOooo) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public AaaaBbbbCcccEntityBuilder(sbyte eeeeFfffGggg=1, short iiiiJjjjKkkk=2, int mmmmNnnnOooo=3) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public AaaaBbbbCcccEntityBuilder(AaaaBbbbCcccEntity that) {
            this.eeeeFfffGggg = that.EeeeFfffGggg;
            this.iiiiJjjjKkkk = that.IiiiJjjjKkkk;
            this.mmmmNnnnOooo = that.MmmmNnnnOooo;
        }

        public AaaaBbbbCcccEntity Build() {
        }

    }

}
