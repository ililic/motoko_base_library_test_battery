// Array
// Functions on Bool
import Bool "mo:base/Bool";
import Result "mo:base/Result";
import Int "mo:base/Int";
import Text "mo:base/Text";

actor BoolTests {

    public func testToText(x : Bool) : async Text {
        return Bool.toText(x);
    };

    public func testLogand(x : Bool, y : Bool) : async Bool {
        return Bool.logand(x, y);
    };

    public func testLogor(x : Bool, y : Bool) : async Bool {
        return Bool.logor(x, y);
    };

    public func testLogxor(x : Bool, y : Bool) : async Bool {
        return Bool.logxor(x, y);
    };

    public func testLognot(x : Bool) : async Bool {
        return Bool.lognot(x);
    };

    public func testEqual(x : Bool, y : Bool) : async Bool {
        return Bool.equal(x, y);
    };

    public func testNotEqual(x : Bool, y : Bool) : async Bool {
        return Bool.notEqual(x, y);
    };

    public func testCompare(x : Bool, y : Bool) : async {#less; #equal; #greater} {
        return Bool.compare(x, y);
    };
};