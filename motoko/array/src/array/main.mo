// Array
// Functions on Arrays
import Array "mo:base/Array";
import Result "mo:base/Result";
import Int "mo:base/Int";
import Text "mo:base/Text";

actor ArrayTests {

    public func testEqual(a : [Text], b : [Text]) : async Bool {
        return Array.equal<Text>(a, b, Text.equal);
    };

    public func testAppend(xs : [Text], ys : [Text]) : async [Text] {
        return Array.append<Text>(xs, ys);
    };

    func chain_func(city: Text) : [Nat] {
      // Stub dummy postal codes for NYC and Seattle
      return [10128, 98109];
    };

    public func testChain(xs : [Text]) : async [Nat] {
        return Array.chain<Text, Nat>(xs, chain_func);
    };

    func filter_func(city: Text) : Bool {
        return Text.equal(city, "New York");
    };

    public func testFilter(xs : [Text]) : async [Text] {
        return Array.filter<Text>(xs, filter_func);
    };

    func map_filter_func(city: Text) : ?Nat {
        // Dummy map filter that just returns 1
        return ?1;
    };

    public func testMapFilter(xs : [Text]) : async [Nat] {
        return Array.mapFilter<Text, Nat>(xs, map_filter_func);
    };

// func testFoldLeft(xs : [Text], initial : Nat, f : (Nat, Text) -> Nat) : Nat {

// };

// func testFoldRight(xs : [Text], initial : Nat, f : (Text, Nat) -> Nat) : Nat {

// };

    func find_predicate_func(city: Text) : Bool {
        // Find a city whose name is longer than 8 letters
        return city.size() > 8;
    };

    public func testFind(xs : [Text]) : async ?Text {
        return Array.find<Text>(xs, find_predicate_func);
    };

// func testFreeze(xs : [var Text]) : [Text] {

// };

    public func testFlatten(xs : [[Text]]) : async [Text] {
        return Array.flatten<Text>(xs);
    };

    func map_func(city: Text) : Nat {
        // Return the length of the city's name
        return city.size();
    };

    public func testMap(xs : [Text]) : async [Nat] {
        return Array.map<Text, Nat>(xs, map_func);
    };

// func testMapEntries(xs : [Text], f : (Text, Nat) -> Nat) : [Nat] {

// };

// func testMapResult(xs : [Text], f : Text -> Result.Result<R, E>) : Result.Result<[R], E> {

// };

   public func testMake(x : Text) : async [Text] {
        return Array.make<Text>(x);
    };

// func testVals(xs : [Text]) : I.Iter<Text> {

// };

// func testKeys(xs : [Text]) : I.Iter<Nat> {

// };

// func testThaw(xs : [Text]) : [var Text] {

// };

// func testInit(size : Nat, initVal : Text) : [var Text] {

// };

// func testTabulate(size : Nat, gen : Nat -> Text) : [Text] {

// };

// func testTabulateVar (size : Nat, gen : Nat -> Text) : [var Text] {

// };
};